// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME dIuscms_datadId3dIreshmardICMSSW_13_0_13dIsrcdIiDMedIpython_analysisdIcondordIskimming_rdfdIAutoDict_ROOT__VecOps__RVec_string__cxx_ACLiC_dict
#define R__NO_DEPRECATION

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// The generated code does not explicitly qualify STL entities
namespace std {} using namespace std;

// Header files passed as explicit arguments
#include "/uscms_data/d3/reshmar/CMSSW_13_0_13/src/iDMe/python_analysis/condor/skimming_rdf/AutoDict_ROOT__VecOps__RVec_string_.cxx"

// Header files passed via #pragma extra_include

namespace ROOT {
   static TClass *ROOTcLcLVecOpscLcLRVeclEstringgR_Dictionary();
   static void ROOTcLcLVecOpscLcLRVeclEstringgR_TClassManip(TClass*);
   static void *new_ROOTcLcLVecOpscLcLRVeclEstringgR(void *p = nullptr);
   static void *newArray_ROOTcLcLVecOpscLcLRVeclEstringgR(Long_t size, void *p);
   static void delete_ROOTcLcLVecOpscLcLRVeclEstringgR(void *p);
   static void deleteArray_ROOTcLcLVecOpscLcLRVeclEstringgR(void *p);
   static void destruct_ROOTcLcLVecOpscLcLRVeclEstringgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ROOT::VecOps::RVec<string>*)
   {
      ROOT::VecOps::RVec<string> *ptr = nullptr;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(ROOT::VecOps::RVec<string>));
      static ::ROOT::TGenericClassInfo 
         instance("ROOT::VecOps::RVec<string>", -2, "ROOT/RVec.hxx", 1453,
                  typeid(ROOT::VecOps::RVec<string>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &ROOTcLcLVecOpscLcLRVeclEstringgR_Dictionary, isa_proxy, 4,
                  sizeof(ROOT::VecOps::RVec<string>) );
      instance.SetNew(&new_ROOTcLcLVecOpscLcLRVeclEstringgR);
      instance.SetNewArray(&newArray_ROOTcLcLVecOpscLcLRVeclEstringgR);
      instance.SetDelete(&delete_ROOTcLcLVecOpscLcLRVeclEstringgR);
      instance.SetDeleteArray(&deleteArray_ROOTcLcLVecOpscLcLRVeclEstringgR);
      instance.SetDestructor(&destruct_ROOTcLcLVecOpscLcLRVeclEstringgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< ROOT::VecOps::RVec<string> >()));

      ::ROOT::AddClassAlternate("ROOT::VecOps::RVec<string>","ROOT::VecOps::RVec<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >");
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ROOT::VecOps::RVec<string>*)
   {
      return GenerateInitInstanceLocal((ROOT::VecOps::RVec<string>*)nullptr);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ROOT::VecOps::RVec<string>*)nullptr); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *ROOTcLcLVecOpscLcLRVeclEstringgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const ROOT::VecOps::RVec<string>*)nullptr)->GetClass();
      ROOTcLcLVecOpscLcLRVeclEstringgR_TClassManip(theClass);
   return theClass;
   }

   static void ROOTcLcLVecOpscLcLRVeclEstringgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_ROOTcLcLVecOpscLcLRVeclEstringgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ROOT::VecOps::RVec<string> : new ROOT::VecOps::RVec<string>;
   }
   static void *newArray_ROOTcLcLVecOpscLcLRVeclEstringgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) ROOT::VecOps::RVec<string>[nElements] : new ROOT::VecOps::RVec<string>[nElements];
   }
   // Wrapper around operator delete
   static void delete_ROOTcLcLVecOpscLcLRVeclEstringgR(void *p) {
      delete ((ROOT::VecOps::RVec<string>*)p);
   }
   static void deleteArray_ROOTcLcLVecOpscLcLRVeclEstringgR(void *p) {
      delete [] ((ROOT::VecOps::RVec<string>*)p);
   }
   static void destruct_ROOTcLcLVecOpscLcLRVeclEstringgR(void *p) {
      typedef ROOT::VecOps::RVec<string> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ROOT::VecOps::RVec<string>

namespace {
  void TriggerDictionaryInitialization_AutoDict_ROOT__VecOps__RVec_string__cxx_ACLiC_dict_Impl() {
    static const char* headers[] = {
"AutoDict_ROOT__VecOps__RVec_string_.cxx",
nullptr
    };
    static const char* includePaths[] = {
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/lcg/root/6.26.11-fec5b250e1cd56b91a094709de26e5b8/include",
"/uscms_data/d3/reshmar/CMSSW_13_0_13/src",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/cmssw/CMSSW_13_0_13/src",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/mctester/1.25.1-43adc37fd0a3365bc6f991c90b74d7fb/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/hydjet2/2.4.3-c74468031010d7c75a15b4af9f5f1cea/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/dd4hep/v01-23x-8c9f79c40c0af370ce5fcdad83ee1ddb/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/herwig7/7.2.2-a4becc9f445057687eeb14500cd741c8/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/tauolapp/1.1.8-8bed7a73d01a87195a23e880da7bccbf/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/sherpa/2.2.12-c7a701d887be15faca23641a24d797c9/include/SHERPA-MC",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lwtnn/2.13-6443dcd675cb29f0fc3ce5fa527a3b7f/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/thepeg/2.2.2-b4cb5de7c5f09f8b21141a1249bceae4/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/pythia8/306-9b96ff06bd00a115810ff75b3e3eb065/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/xrootd/5.5.1-0f563ccc18e94a7e64a93dc184abaae9/include/xrootd/private",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/starlight/r193-32562079cd983e33c0d7cea2e4ef8e3c/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/rivet/3.1.7-e8f0856ea545f46143f13c14e4ab19b5/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/highfive/2.3.1-7f6cb0002d1362228aad3a565ade3fe1/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/geant4/10.7.2-0a5e38613906bb5debc9753e0e1d40b3/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/classlib/3.1.3-52a2fe4d34a5f733d734f75ee05cb886/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lhapdf/6.4.0-e019996650b819a0fc60be6587a245af/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/alpaka/develop-20230621-0e0add1a69915f1c9fab0fe26623c322/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/tkonlinesw/4.2.0-1_gcc7-ee95d41b479e7090b9bdc81f11d8537e/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/pcre2/10.36-88c59c64ebe54b36ea4626d5827d6026/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/libungif/4.1.4-6b4f3e28660c3a9d4e75854eb8da0012/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/libtiff/4.0.10-379c6010fabb72a8b7d2ebca2df35c1d/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/libpng/1.6.37-a2ff0f76300cbef7e51b77d816ff554a/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/frontier_client/2.9.1-ee993126dcdd1f2f1cc5df6ef8035e5f/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/pcre/8.43-5dcc901acc02f624b22dd9840b2357e8/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/zstd/1.5.2-290d3b726e169356bcb00341a538fea2/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/vdt/0.4.3-26bd784324b069f05218637042354cf4/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/valgrind/3.17.0-7ca83817e7379e83453f913e11e14834/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/utm/utm_0.11.2-de0545016d130fba86b295ac38227fd2/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/sigcpp/3.2.0-50e87bb1933c52adc9bdc81af5f96b5c/include/sigc++-3.0",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/sqlite/3.36.0-0f26675926fd468efdd431be2b62785e/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/pacparser/1.4.0-cbf4a008ddde4856a4762d7e9b1d7846/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/oracle/19.11.0.0.0dbru-092ba337a70a02c4734616a84f842897/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/py3-numpy/1.22.4-aec0a210f14617f175dad913e0d72013/c-api/core/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/meschach/1.2.pCMS1-a6c940d49300e01334c28ef7c2460c02/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/lz4/1.9.2-031da253be076d002e4d6af36bc64212/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/libuuid/2.34-0451b31e1b9a58c6aeefab41c18eea34/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/libjpeg-turbo/2.0.2-217828589b5d70f70e96c4d718c063d7/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/ktjet/1.06-738ae10b9bb784a037c4eecb20593099/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/jemalloc/5.3.0-0416c43bb3ec49c63e8dd3f7c38684a8/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/hls/2019.08-fd724004387c2a6770dc3517446d30d9/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/madgraph5amcatnlo/2.7.3-bfa8c81ef814737bd45adc6fc2d928a2",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/heppdt/3.04.01-1bbda45c67d229c2b2e8a19462c4c3c9/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/hector/1.3.4_patch1-938487bfcffe2e713aa23525cb0ac1fe/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/protobuf/3.15.1-036bf7223636330571398e8740492e00/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/libunwind/1.6.2-master-5661dca2c54f6802e98cc3676ea0f0d6/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/giflib/5.2.0-e928fbc1a732191ff28d8dfbf2e6ee63/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/gdbm/1.10-94fd72446cd6c73834b291fb1d1c6f46/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/freetype/2.10.0-7c6fc6af284a6e94f5e435c9ea3767b9/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/fftw3/3.3.8-5f403c3dc6c4147769a1f10565ec7e26/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/fftjet/1.5.0-1cd7b7c71b42be65b840b68281156a1e/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/fastjet/3.4.0-a31b3d7621aa3e26e075c913ff770207/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/expat/2.1.0-5f6457b4c04e97afec6079bd7d2db998/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/vecgeom/v1.1.17-07b69d717ed40abe6434c19ba70a9983/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/vecgeom/v1.1.17-07b69d717ed40abe6434c19ba70a9983/include/VecGeom",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/xerces-c/3.1.3-96261f23c7d6fbfb7d59be544bd882f3/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/xz/5.2.5-83d0a00b575efd1701e07bedf7977343/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/lcg/root/6.26.11-fec5b250e1cd56b91a094709de26e5b8/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/dcap/2.47.12-ef79ca4ec7d517ad93018edfef3356c2/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/libxml2/2.9.10-0a5b015a5590b04cf3087955ff42a243/include/libxml2",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/curl/7.79.0-5e48e0bf013ba13376a33ec8da72dabc/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/cppunit/1.15.x-c4570d64b509e2e0614dc83d98c1df8c/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/cms/coral/CORAL_2_3_21-0c6298d2d88b04357d1548a007ebd73c/include/LCG",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/clhep/2.4.5.1-47a59842f4586f2cb0f8e5db68e38998/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/zlib/1.2.11-3dfb2715f3608466b74431b80eb9d788/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/pythia6/426-154c9fa9309a9a96c7e05f80622d33eb/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/hepmc/2.06.10-892134cadaa17164a15ce108f11ec15f/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/gsl/2.6-fcf47bcbedd800ca8386c7e2920fa474/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/bz2lib/1.0.6-2c1f18484cb66c30aba7929f2be5e7d4/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/tbb/v2021.8.0-bb5e0283c68ca6d69bd8419f6c08f7b1/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/rocm-rocrand/5.4.3-e3475a4b3c5a437af6279c98f00344a9/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/cuda/11.5.2-66a9473808e7d5863d5bbec0824e2c4a/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/boost/1.80.0-bff81045eb6d0806da34e08d781c05db/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/xgboost/1.6.2-e2fae94cab3f93f96bd60fb839a14344/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/tinyxml2/6.2.0-20b4f0dfd078828bfb8e7fdd5ba85221/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/rdma-core/39.1-7ffd1c7dfa366e47c5ab68e4bc8bc1f1/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/ittnotify/16.06.18-1a2fe4bfd5b3b60634b5c4cb3a739547/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/gosamcontrib/2.0-20150803-001c255025c150fdbe081040c1f49536/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/fmt/8.0.1-557ae4739f3cbc76e428d57162bae99b/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/eigen/82dd3710dac619448f50331c1d6a35da673f764a-b0dc243d10365424e66e60c822ab818e/include/eigen3",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/rocm/5.4.3-54a49cd5963d1f81136e5ec29a9fc8d7/include",
"/usr/local/include",
"/usr/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/lcg/root/6.26.11-fec5b250e1cd56b91a094709de26e5b8/etc/",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/lcg/root/6.26.11-fec5b250e1cd56b91a094709de26e5b8/etc//cling",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/lcg/root/6.26.11-fec5b250e1cd56b91a094709de26e5b8/etc//cling/plugins/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/lcg/root/6.26.11-fec5b250e1cd56b91a094709de26e5b8/include/",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/python3/3.9.14-76a14295dd5255228210eb596893b98c/include",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/external/python3/3.9.14-76a14295dd5255228210eb596893b98c/include/python3.9",
"/uscms_data/d3/reshmar/CMSSW_13_0_13/src/iDMe/python_analysis/condor/skimming_rdf/",
"/cvmfs/cms.cern.ch/el8_amd64_gcc11/lcg/root/6.26.11-fec5b250e1cd56b91a094709de26e5b8/include/",
"/uscms_data/d3/reshmar/CMSSW_13_0_13/src/iDMe/python_analysis/condor/skimming_rdf/",
nullptr
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "AutoDict_ROOT__VecOps__RVec_string__cxx_ACLiC_dict dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_AutoLoading_Map;
namespace std{template <class _CharT> struct __attribute__((annotate("$clingAutoload$bits/char_traits.h")))  __attribute__((annotate("$clingAutoload$string")))  char_traits;
}
namespace std{template <typename > class __attribute__((annotate("$clingAutoload$bits/memoryfwd.h")))  __attribute__((annotate("$clingAutoload$string")))  allocator;
}
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "AutoDict_ROOT__VecOps__RVec_string__cxx_ACLiC_dict dictionary payload"

#ifndef __ACLIC__
  #define __ACLIC__ 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
// Inline headers
#include "AutoDict_ROOT__VecOps__RVec_string_.cxx"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[] = {
"ROOT::VecOps::RVec<string>", payloadCode, "@",
nullptr
};
    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("AutoDict_ROOT__VecOps__RVec_string__cxx_ACLiC_dict",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_AutoDict_ROOT__VecOps__RVec_string__cxx_ACLiC_dict_Impl, {}, classesHeaders, /*hasCxxModule*/false);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_AutoDict_ROOT__VecOps__RVec_string__cxx_ACLiC_dict_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_AutoDict_ROOT__VecOps__RVec_string__cxx_ACLiC_dict() {
  TriggerDictionaryInitialization_AutoDict_ROOT__VecOps__RVec_string__cxx_ACLiC_dict_Impl();
}
